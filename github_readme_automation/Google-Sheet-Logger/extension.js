// The module 'vscode' contains the VS Code extensibility API
// Import the module and reference it with the alias vscode in your code below
const vscode = require('vscode');
const { basename } = require('path');
const { GoogleToken } = require('gtoken');
const axios = require('axios');

//Importing config files.
const config = vscode.workspace;
let email = config.getConfiguration('email').get('GoogleServiceAccountEmail')
let sheetID = config.getConfiguration('sheetId').get('LocatedInGoogleSheetUrl')
let sheetName = config.getConfiguration('sheetName').get('theNameOfTheSheet')
let keyP12 = config.getConfiguration('keyFile').get('p12File')


// this method is called when your extension is activated
// your extension is activated the very first time the command is executed

/**
 * @param {vscode.ExtensionContext} context
 */
function activate(context) {

	// Use the console to output diagnostic information (console.log) and errors (console.error)
	// This line of code will only be executed once when your extension is activated
	console.log('Congratulations, your extension "googlesheetlogger" is now active!');

	// The command has been defined in the package.json file
	// Now provide the implementation of the command with  registerCommand
	// The commandId parameter must match the command field in package.json

	//messy affff... code starts here. maybe the most shit code you have ever seen! sorry I am still new to this game!

	//those values I want to log on gsheet

//	const config = vscode.workspace.getConfiguration('launch', vscode.workspace.workspaceFolders[0].uri);


	//there we get a token.
	async function add_data() {

		//get token from here....
		function getToken() {
			// @ts-ignore
			let file = context.asAbsolutePath(keyP12)
			return new Promise((resolve, reject) => {
				const gtoken = new GoogleToken({
					scope: ['https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive.file'],
					keyFile: file,
					email: `${email}`

				});

				gtoken.getToken((err, tokens) => {
					if (err) {
						console.log(err);
						reject('Error')
					}
					resolve(tokens);
				})
			})

		}

		let vsDetail = function () {
			let fileName = null;
			let workspaceName = null;
			if (vscode.window.activeTextEditor) {
				fileName = basename(vscode.window.activeTextEditor.document.fileName);
				workspaceName = vscode.workspace.name;
				//only using FILENAME and WORKSPACENAME For now.
			}
			return {
				fName: fileName,
				wsName: workspaceName
			}
		}

		let myDataA = vsDetail().fName
		let myDataB = vsDetail().wsName
		let sID = sheetID
		let sName = sheetName

		let time = () => {
			return new Promise((resolve, reject) => {
				let time = new Date().getTime();
				let minute = 1000 * 60
				let now = Math.round(time / minute);
				resolve(now)
			})
		}

		let token_object = await getToken();
		let currentTime = await time();
		let access = token_object.access_token
		console.log(`token_accessed: ${access}`);

		// @ts-ignore
		axios(
			{
				method: "post",
				url: `https://sheets.googleapis.com/v4/spreadsheets/${sID}/values/${sName}:clear`,
				headers: {
					Authorization: `Bearer ${access}`
				}
			}
		)
			.catch((error) => {
				if (error) {
					console.log(error)
				}
			})

		// @ts-ignore
		setTimeout(() => {
			// @ts-ignore
			axios(
				{
					method: "post",
					url: `https://sheets.googleapis.com/v4/spreadsheets/${sID}/values/${sName}:append`,
					params: {
						includeValuesInResponse: true,
						valueInputOption: "USER_ENTERED"
					},
					headers: {
						Authorization: `Bearer ${access}`
					},
					data: {
						values: [[`${myDataA}`, `${myDataB}`, `${currentTime}`]]
					}
				}
			)
				.catch((error) => {
					if (error) {
						console.log(error)
					}
				})
		}, 3000)
	}

	// set timeinterval...
	add_data()
	setInterval(() => {
		add_data()
	}, 300000); //updates every 3 minutes...
	//or restart to update...


}

exports.activate = activate;

// this method is called when your extension is deactivated
function deactivate() { }

module.exports = {
	activate,
	deactivate
}
