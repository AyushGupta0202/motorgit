![Motorgit Logo](motorgit_logo.png)

# 🚀 Motorgit

## 🌟 Overview

Motorgit is a smart tool designed to automate GitHub repository creations and updates with a single command. It simplifies the workflow for developers by integrating common tasks into a streamlined command-line interface.

## 📋 Table of Contents

1. [✨ Features](#features)
2. [⚙️ Installation](#installation)
    - [📦 Install from pip](#install-from-pip)
    - [🔑 Configure GitHub Credentials](#configure-personal-access-token-pat-username-and-email)
      - [Interactive Setup Wizard](#1-interactive-setup-wizard-recommended)
      - [Manual Login/Logout](#2-manualloginlogout)
      - [Configuration Management](#3-configuration-management)
      - [Environment Variables](#4-environment-variables-legacy-method)
    - [🔧 Install Locally](#install-locally)
3. [📚 Usage](#usage)
    - [🆕 Create a New Repository](#create-a-new-repository)
    - [🔄 Update Repository](#update-repository)
    - [🔍 Shell Completion](#shell-completion)
4. [🤝 Contribution](#contribution)
5. [📜 License](#license)
6. [👤 Author](#author)

## ✨ Features

- **🆕 Create New Repositories:** Quickly create new GitHub repositories from the command line.
- **🔄 Update Repositories:** Easily update existing repositories with a single command.
- **⚡ Efficient Workflow:** Automates repetitive tasks, saving time and reducing errors.
- **🔍 Tab Completion:** Support for Bash, Zsh, and Fish shell completion.
- **🔐 Secure Credentials:** Store GitHub credentials securely using system keyring.

## ⚙️ Installation

### 📦 Install from pip

To install Motorgit using pip, run:

```
pip install motorgit
```
### 🔑 Configure GitHub Credentials

Motorgit provides multiple secure ways to configure your GitHub credentials:

#### 1. Interactive Setup Wizard (Recommended)

Run the setup wizard to configure your credentials interactively:

```bash
motorgit setup
```

This will prompt for your GitHub username, email, and access token, and store them securely using your system's credential store.

#### 2. Manual Login/Logout

You can also use the login/logout commands to manage your credentials:

```bash
# Store credentials securely
motorgit login

# Remove stored credentials
motorgit logout
```

> **Note:**
> Use `motorgit setup` for first-time or full configuration (including credentials and other settings).
> Use `motorgit login` if you only want to update your GitHub credentials without changing other settings.

| Command           | Prompts for Credentials | Stores Credentials | Configures Other Settings | Intended Use                |
|-------------------|:----------------------:|:------------------:|:------------------------:|-----------------------------|
| `motorgit setup`  |          Yes           |        Yes         |           Yes            | First-time or full setup    |
| `motorgit login`  |          Yes           |        Yes         |           No             | Update credentials only     |

#### 3. Configuration Management

View or update configuration settings:

```bash
# View all configuration
motorgit config

# View specific configuration
motorgit config github_username

# Update configuration
motorgit config github_username yourusername
```

#### 4. Environment Variables (Legacy Method)

For backward compatibility or CI/CD environments, you can still use environment variables.
Add the following lines to your **.bashrc** or **.zshrc** file:

```bash
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

![Motorgit Terminal Example](motorgit_terminal.png)

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

### 🔍 Shell Completion

Motorgit supports shell tab completion for Bash, Zsh, and Fish using Click's built-in shell completion system. To enable shell completion, follow the instructions for your shell:

#### Bash
Add this to your `~/.bashrc`:
```bash
eval "$(_MOTORGIT_COMPLETE=bash_source motorgit)"
```
Or, to generate and source a static script:
```bash
_MOTORGIT_COMPLETE=bash_source motorgit > ~/.motorgit-complete.bash
. ~/.motorgit-complete.bash
```

#### Zsh
Add this to your `~/.zshrc`:
```zsh
eval "$(_MOTORGIT_COMPLETE=zsh_source motorgit)"
```
Or, to generate and source a static script:
```zsh
_MOTORGIT_COMPLETE=zsh_source motorgit > ~/.motorgit-complete.zsh
. ~/.motorgit-complete.zsh
```

#### Fish
Add this to `~/.config/fish/completions/motorgit.fish`:
```fish
_MOTORGIT_COMPLETE=fish_source motorgit > ~/.config/fish/completions/motorgit.fish
```

After modifying your shell configuration, start a new shell session or source the relevant file to activate completion.

For more details, see the [Click Shell Completion documentation](https://click.palletsprojects.com/en/stable/shell-completion/).

## 🤝 Contribution
Contributions are welcome! Please open an issue or submit a pull request on GitHub.

**1. 🍴 Fork the repository**

**2. 🌿 Create a new branch:** `git checkout -b my-new-feature`

**3. 💾 Commit your changes:** `git commit -am 'Add some feature'`

**4. 📤 Push to the branch:** `git push origin my-new-feature`

**5. 🔁 Create a new Pull Request**

or after cloning use **motorgit** commands itself!

## 📜 License
Motorgit is licensed under the MIT License. See the [LICENSE_MOTORGIT.txt](https://github.com/AyushGupta0202/motorgit/blob/main/LICENSE_MOTORGIT.txt) file for more details.

> **Note:** The license file was renamed from LICENSE.txt to LICENSE_MOTORGIT.txt to avoid PyPI upload metadata issues. This ensures smooth uploads and full license compliance.

## 👤 Author
Ayush Gupta

For any inquiries, feel free to contact: ayushg430@gmail.com

Made with ❤️ using ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) click