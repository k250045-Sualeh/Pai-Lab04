class PasswordVault:
    def __init__(self, username, password):
        self.username = username           
        self._vault_status = "Locked"        # Protected variable
        self.__password = password           # Private variable

    def change_password(self, old_password, new_password):

        if old_password == self.__password:
            self.__password = new_password
            self._vault_status = "Unlocked"
            print("Password changed successfully.")
        else:
            print("Incorrect old password. Password change denied.")

    def verify_password(self, entered_password):
        
        if entered_password == self.__password:
            self._vault_status = "Unlocked"
            print("Access Granted")
        else:
            self._vault_status = "Locked"
            print("Access Denied")

    def display_status(self):
        """Displays the current status of the vault."""
        print(f"Username     : {self.username}")
        print(f"Vault Status : {self._vault_status}")
        print("-" * 40)


vault = PasswordVault("admin user", "Secure@123")

vault.display_status()

vault.verify_password("wrongpass")
vault.verify_password("Secure@123")

vault.display_status()

vault.change_password("wrongoldpass", "NewPass@ahhhh")
vault.change_password("Secure@123", "NewPass@ahhhh")

vault.display_status()

vault.verify_password("NewPass@ahhhh")