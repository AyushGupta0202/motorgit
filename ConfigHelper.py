import os
import json
import Constants

class ConfigHelper:
    """Helper for managing Motorgit configuration files"""
    
    def __init__(self):
        self.config_dir = os.path.expanduser("~/.motorgit")
        self.config_file = os.path.join(self.config_dir, "config.json")
        self.ensure_config_exists()
    
    def ensure_config_exists(self):
        """Ensure config directory and file exist"""
        if not os.path.exists(self.config_dir):
            os.makedirs(self.config_dir)
        
        if not os.path.exists(self.config_file):
            default_config = {
                "credential_store": "keyring",  # Options: keyring, env
                "github_username": "",
                "github_email": ""
            }
            self.save_config(default_config)
    
    def load_config(self):
        """Load configuration from file"""
        try:
            with open(self.config_file, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading config: {e}")
            return {}
    
    def save_config(self, config):
        """Save configuration to file"""
        try:
            with open(self.config_file, 'w') as f:
                json.dump(config, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving config: {e}")
            return False
    
    def update_config(self, key, value):
        """Update a specific config value"""
        config = self.load_config()
        config[key] = value
        return self.save_config(config)
    
    def get_config(self, key, default=None):
        """Get a specific config value"""
        config = self.load_config()
        return config.get(key, default) 