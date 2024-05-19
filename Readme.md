# 🚀 Motorgit

## 🌟 Overview

Motorgit is a smart tool designed to automate GitHub repository creations and updates with a single command. It simplifies the workflow for developers by integrating common tasks into a streamlined command-line interface.

## 📋 Table of Contents

1. [✨ Features](#features)
2. [⚙️ Installation](#installation)
    - [📦 Install from pip](#install-from-pip)
    - [🔑 Configure Personal Access Token (PAT), Username, and Email](#configure-personal-access-token-pat-username-and-email)
    - [🔧 Install Locally](#install-locally)
3. [📚 Usage](#usage)
    - [🆕 Create a New Repository](#create-a-new-repository)
    - [🔄 Update Repository](#update-repository)
4. [🤝 Contribution](#contribution)
5. [📜 License](#license)
6. [👤 Author](#author)

## ✨ Features

- **🆕 Create New Repositories:** Quickly create new GitHub repositories from the command line.
- **🔄 Update Repositories:** Easily update existing repositories with a single command.
- **⚡ Efficient Workflow:** Automates repetitive tasks, saving time and reducing errors.

## ⚙️ Installation

### 📦 Install from pip

To install Motorgit using pip, run:

```
pip install motorgit
```
### 🔑 Configure Personal Access Token (PAT), Username, and Email
Motorgit requires your GitHub personal access token (PAT), username, and email for authentication. Add the following lines to your **.bashrc** or **.zshrc** file:

```
export GITHUB_ACCESSTOKEN='your_personal_access_token'
export GITHUB_USERNAME='your_github_username'
export GITHUB_USEREMAIL='your_email@example.com'
```
After adding the lines, reload your shell configuration:
```
source ~/.bashrc  # For bash users
```
```
source ~/.zshrc   # For zsh users
```
### 🔧 Install Locally
To install Motorgit locally from the source code, follow these steps:

#### 1. Clone the repository:
```
git clone https://github.com/AyushGupta0202/motorgit.git
cd motorgit
```
#### 2. Install in editable mode:
```
pip install --editable .
```
## 📚 Usage
### Usage 🆕 Create a New Repository
To create a new repository, use the following command:
```
motorgit createNewRepo
```
This command has optional parameters for folder name and whether it should be made as a private repository or not.
And then it will create a new repository on GitHub with the specified settings.

#### Example
```
motorgit createNewRepo [-n foldername] [-p privaterepo]
```

### 🔄 Update Repository
To update an existing repository with a commit message, use:

```
motorgit updateRepo -m "Motorgit Commit"
```
This command will add changes to the repository and commit them with the provided message.
#### Example
```
motorgit updateRepo [-m commitmessage] [-b branchname]
```

## 🤝 Contribution
Contributions are welcome! Please open an issue or submit a pull request on GitHub.

**1. 🍴 Fork the repository**

**2. 🌿 Create a new branch:** `git checkout -b my-new-feature`

**3. 💾 Commit your changes:** `git commit -am 'Add some feature'`

**4. 📤 Push to the branch:** `git push origin my-new-feature`

**5. 🔁 Create a new Pull Request**

or after cloning use **motorgit** commands itself!

## 📜 License
Motorgit is licensed under the MIT License. See the [LICENSE](https://github.com/AyushGupta0202/motorgit/blob/main/LICENSE.txt) file for more details.

## 👤 Author
Ayush Gupta

For any inquiries, feel free to contact: ayushg430@gmail.com

Made with ❤️ using ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) click