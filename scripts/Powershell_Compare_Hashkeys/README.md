# Powershell_Compare_Hashkeys

## About
With this tool you can check if the Hash of a downloaded file is the same as indicated on the Downloadsource

## Usage
1. Open Powershell
2. Navigate to the Path of the script
3. `.\Compare_Hashkeys.ps1 <Alogithm> <Path of Downloaded File> <Hashcode for refernce>`

E.g.
`.\Compare_Hashkeys.ps1 SHA512 .\test.txt C034748....`

## Outputs
`Hashes are identical!`  
or  
`Hashes are NOT identical!`

### Available Algorithms
* SHA1
* SHA256
* SHA384
* SHA512
* MD5
