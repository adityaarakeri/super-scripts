const path = require('path');
const fs = require('fs');
const crypto = require('crypto');
const workingDir = 'hashes';
!fs.existsSync(workingDir) ? fs.mkdirSync(workingDir) : undefined;
const args = process.argv.slice(2);
const lastRunJsonfileName = `${args[0]}.json`;
const newRunJsonfileName = `${args[0]}.json`;
const lastRunFiles = fs.existsSync(path.join(workingDir, lastRunJsonfileName))
  ? JSON.parse(fs.readFileSync(path.join(workingDir, lastRunJsonfileName), 'utf8'))
  : {};
const filesToSkip = [lastRunJsonfileName, 'package-lock.json'];
const dirsToSkip = ['.git', 'node_modules', 'dist'];
const newRunFiles = {};

const getFileAndHashFormDir = (dir) => {
  fs.readdirSync(dir).forEach((file) => {
    let fullPath = path.join(dir, file);
    if (!dirsToSkip.some((dir) => path.dirname(fullPath).indexOf(dir) >= 0) && !filesToSkip.includes(file)) {
      if (fs.lstatSync(fullPath).isDirectory()) {
        getFileAndHashFormDir(fullPath);
      } else {
        newRunFiles[fullPath] = getFileHash(fullPath);
      }
    }
  });
};

const getFileHash = (fullPath) => {
  const data = fs.readFileSync(fullPath);
  return checksum(data, 'sha1');
};

const checksum = (str, algorithm, encoding) => {
  return crypto
    .createHash(algorithm || 'md5')
    .update(str, 'utf8')
    .digest(encoding || 'hex');
};

const writeFile = (fileName, data) => fs.writeFileSync('./' + fileName, data);

const areDifferent = (lastRunFiles, newRunFiles) => {
  let different = Object.keys(lastRunFiles).length !== Object.keys(newRunFiles).length;
  Object.keys(newRunFiles).forEach((key) => {
    if (!different) {
      different = !lastRunFiles[key] ? true : lastRunFiles[key] !== newRunFiles[key];
    }
  });
  return different;
};

const removeIfExist = (fileName) => {
  if (fs.existsSync(fileName)) {
    fs.unlinkSync(fileName);
  }
};

const logGreen = (text) => console.log('\x1b[32m%s\x1b[0m', text);

// main
if (fs.lstatSync(process.cwd(), args[0]).isDirectory()) {
  getFileAndHashFormDir('./' + args[0]);
  logGreen('--------------------------');
  const different = areDifferent(lastRunFiles, newRunFiles);
  if (!!different) {
    removeIfExist(path.join(workingDir, lastRunJsonfileName));
    writeFile(path.join(workingDir, newRunJsonfileName), JSON.stringify(newRunFiles));
    logGreen(`${args[0]} is dirty`);
    logGreen('--------------------------');
  } else {
    logGreen(`${args[0]} is pristine`);
    logGreen('--------------------------\n');
    process.exit(1);
  }
}
