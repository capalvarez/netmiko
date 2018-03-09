from netmiko.cisco_base_connection import CiscoSSHConnection


class DellDNOS6SSH(CiscoSSHConnection):
    """Dell N Series Driver. Supports DNOS6"""
    def exit_enable_mode(self, exit_command='exit'):
        """Exits enable (privileged exec) mode."""
        if self.check_enable_mode():
            return super(CiscoSSHConnection, self).exit_enable_mode(exit_command=exit_command)
