#!/usr/bin/env python3
"""Pattoo classes that manage various configurations."""

import os.path
import os
import sys

# Import project libraries
from pattoo.shared import files
from pattoo.shared import log


class Config(object):
    """Class gathers all configuration information."""

    def __init__(self):
        """Initialize the class.

        Args:
            None

        Returns:
            None

        """
        # Update the configuration directory

        config_directory = '{}/etc'.format(files.root_directory())

        # Return data
        self._config_dict = files.read_yaml_files(config_directory)

    def polling_interval(self):
        """Get interval.

        Args:
            None

        Returns:
            result: result

        """
        # Get result
        key = 'main'
        sub_key = 'interval'
        intermediate = search(key, sub_key, self._config_dict, die=False)

        # Default to 300
        if intermediate is None:
            result = 300
        else:
            result = int(intermediate)
        return result

    def api_ip_address(self):
        """Get api_ip_address.

        Args:
            None

        Returns:
            result: result

        """
        # Initialize key variables
        key = 'remote_api'
        sub_key = 'api_ip_address'

        # Get result
        result = search(key, sub_key, self._config_dict, die=False)
        if result is None:
            result = 'localhost'
        return result

    def api_ip_bind_port(self):
        """Get api_ip_bind_port.

        Args:
            None

        Returns:
            result: result

        """
        # Initialize key variables
        key = 'remote_api'
        sub_key = 'api_ip_bind_port'

        # Get result
        intermediate = search(key, sub_key, self._config_dict, die=False)
        if intermediate is None:
            result = 6000
        else:
            result = int(intermediate)
        return result

    def api_uses_https(self):
        """Get api_uses_https.

        Args:
            None

        Returns:
            result: result

        """
        # Initialize key variables
        key = 'remote_api'
        sub_key = 'api_uses_https'

        # Get result
        result = search(key, sub_key, self._config_dict, die=False)
        if result is None:
            result = False
        return result

    def api_uri(self):
        """Get api_uri.

        Args:
            None

        Returns:
            result: result

        """
        # Initialize key variables
        key = 'remote_api'
        sub_key = 'api_uri'

        # Get result
        received = search(key, sub_key, self._config_dict, die=False)
        if received is None:
            received = 'pattoo/api/v1.0'

        # Trim leading slash if exists
        if received.startswith('/') is True:
            received = received[1:]
        if received.endswith('/') is True:
            received = received[:-1]

        # Return
        result = received
        return result

    def api_server_url(self, agent_id):
        """Get pattoo server's remote URL.

        Args:
            agent_id: Agent ID

        Returns:
            result: URL.

        """
        # Construct URL for server
        if self.api_uses_https() is True:
            prefix = 'https://'
        else:
            prefix = 'http://'

        # Return
        result = (
            '{}{}:{}/{}/receive/{}'.format(
                prefix, self.api_ip_address(),
                self.api_ip_bind_port(), self.api_uri(), agent_id))
        return result

    def log_directory(self):
        """Get log_directory.

        Args:
            None

        Returns:
            result: result

        """
        # Get result
        sub_key = 'log_directory'
        result = None
        key = 'main'

        # Get new result
        _result = search(key, sub_key, self._config_dict)

        # Expand linux ~ notation for home directories if provided.
        result = os.path.expanduser(_result)

        # Check if value exists. We cannot use logging as it requires a
        # log directory location to work properly
        if os.path.isdir(result) is False:
            log_message = (
                'log_directory: "{}" '
                'in configuration doesn\'t exist!'.format(result))
            print(log_message)
            sys.exit(1)

        # Return
        return result

    def log_file(self):
        """Get log_file.

        Args:
            None

        Returns:
            result: result

        """
        _log_directory = self.log_directory()
        result = '{}{}pattoo.log'.format(_log_directory, os.sep)
        return result

    def log_file_api(self):
        """Get log_file_api.

        Args:
            None

        Returns:
            result: result

        """
        # Get result
        _log_directory = self.log_directory()
        result = '{}{}pattoo-api.log'.format(_log_directory, os.sep)
        return result

    def log_level(self):
        """Get log_level.

        Args:
            None

        Returns:
            result: result

        """
        # Get result
        sub_key = 'log_level'
        key = 'main'
        result = None

        # Return
        intermediate = search(key, sub_key, self._config_dict, die=False)
        if intermediate is None:
            result = 'debug'
        else:
            result = '{}'.format(intermediate).lower()
        return result

    def language(self):
        """Get language.

        Args:
            None

        Returns:
            result: result

        """
        # Get result
        sub_key = 'language'
        result = None
        key = 'main'

        # Get new result
        result = search(key, sub_key, self._config_dict)

        # Return
        return result

    def cache_directory(self):
        """Determine the cache_directory.

        Args:
            None

        Returns:
            value: configured cache_directory

        """
        # Initialize key variables
        key = 'main'
        sub_key = 'cache_directory'

        # Get result
        _value = search(key, sub_key, self._config_dict)

        # Expand linux ~ notation for home directories if provided.
        value = os.path.expanduser(_value)

        # Create directory if it doesn't exist
        files.mkdir(value)

        # Return
        return value

    def agent_cache_directory(self, agent_program):
        """Get agent_cache_directory.

        Args:
            agent_program: Name of agent

        Returns:
            result: result

        """
        # Get result
        result = '{}/{}'.format(self.cache_directory(), agent_program)

        # Create directory if it doesn't exist
        files.mkdir(result)

        # Return
        return result


class ConfigSpoked(Config):
    """Template for PATTOO_OS_AUTONOMOUSD configuration information."""

    def __init__(self):
        """Initialize the class.

        Args:
            None

        Returns:
            None

        """
        # Instantiate the Config parent
        Config.__init__(self)

    def listen_address(self):
        """Get listen_address.

        Args:
            None

        Returns:
            result: result

        """
        # Placeholder
        pass

    def ip_bind_port(self):
        """Get ip_bind_port.

        Args:
            None

        Returns:
            result: result

        """
        # Placeholder
        pass


class ConfigHubd(Config):
    """Template for PATTOO_OS_HUBD configuration information."""

    def __init__(self):
        """Initialize the class.

        Args:
            None

        Returns:
            None

        """
        # Instantiate the Config parent
        Config.__init__(self)

    def devices(self):
        """Get devices.

        Args:
            None

        Returns:
            result: result

        """
        # Placeholder
        pass


def search(key, sub_key, config_dict, die=True):
    """Get config parameter from YAML.

    Args:
        key: Primary key
        sub_key: Secondary key
        config_dict: Dictionary to explore
        die: Die if true and the result encountered is None

    Returns:
        result: result

    """
    # Get result
    result = None

    # Verify config_dict is indeed a dict.
    # Die safely as log_directory is not defined
    if isinstance(config_dict, dict) is False:
        log.log2die_safe(1021, 'Invalid configuration file. YAML not found')

    # Get new result
    if key in config_dict:
        # Make sure we don't have a None value
        if config_dict[key] is None:
            log_message = (
                '{}: value in configuration is blank. Please fix'.format(key))
            log.log2die_safe(1022, log_message)

        # Get value we need
        if sub_key in config_dict[key]:
            result = config_dict[key][sub_key]

    # Error if not configured
    if result is None and die is True:
        log_message = (
            '{}:{} not defined in configuration'.format(key, sub_key))
        log.log2die_safe(1016, log_message)

    # Return
    return result
