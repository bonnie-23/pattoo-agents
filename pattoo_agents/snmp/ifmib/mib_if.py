#!/usr/bin/env python3
"""Class interacts with devices supporting IfMIB. (32 Bit Counters)."""


from collections import defaultdict

from pattoo_agents.snmp import snmp


class Query(object):
    """Class interacts with devices supporting IfMIB.

    Args:
        None

    Returns:
        None

    Key Methods:

        everything: Returns all needed layer 1 MIB information from the device.
            Keyed by OID's MIB name (primary key), ifIndex (secondary key)

    """

    def __init__(self, snmpvariable):
        """Function for intializing the class.

        Args:
            snmpvariable: SNMPVariable to poll

        Returns:
            None

        """
        # Define query object
        self._query = snmp.SNMP(snmpvariable)

    def everything(self):
        """Get layer 1 data from device using Layer 1 OIDs.

        Args:
            None

        Returns:
            final: Final results

        """
        # Initialize key variables
        final = defaultdict(lambda: defaultdict(dict))

        # Get interface ifDescr data
        _get_data('ifDescr', self.ifdescr, final)

        # Get interface ifAlias data
        _get_data('ifAlias', self.ifalias, final)

        # Get interface ifName data
        _get_data('ifName', self.ifname, final)

        # Get interface ifIndex data
        _get_data('ifIndex', self.ifindex, final)

        # Get interface ifInOctets data
        _get_data('ifInOctets', self.ifinoctets, final)

        # Get interface ifOutOctets data
        _get_data('ifOutOctets', self.ifoutoctets, final)

        # Get interface ifInBroadcastPkts data
        _get_data('ifInBroadcastPkts', self.ifinbroadcastpkts, final)

        # Get interface ifOutBroadcastPkts data
        _get_data('ifOutBroadcastPkts', self.ifoutbroadcastpkts, final)

        # Get interface ifInMulticastPkts data
        _get_data('ifInMulticastPkts', self.ifinmulticastpkts, final)

        # Get interface ifOutMulticastPkts data
        _get_data('ifOutMulticastPkts', self.ifoutmulticastpkts, final)

        # Get interface ifHCOutBroadcastPkts data
        _get_data('ifHCOutBroadcastPkts', self.ifhcoutbroadcastpkts, final)

        # Get interface ifHCOutMulticastPkts data
        _get_data('ifHCOutMulticastPkts', self.ifhcoutmulticastpkts, final)

        # Get interface ifHCOutUcastPkts data
        _get_data('ifHCOutUcastPkts', self.ifhcoutucastpkts, final)

        # Get interface ifHCOutOctets data
        _get_data('ifHCOutOctets', self.ifhcoutoctets, final)

        # Get interface ifHCInBroadcastPkts data
        _get_data('ifHCInBroadcastPkts', self.ifhcinbroadcastpkts, final)

        # Get interface ifHCInMulticastPkts data
        _get_data('ifHCInMulticastPkts', self.ifhcinmulticastpkts, final)

        # Get interface ifHCInUcastPkts data
        _get_data('ifHCInUcastPkts', self.ifhcinucastpkts, final)

        # Get interface ifHCInOctets data
        _get_data('ifHCInOctets', self.ifhcinoctets, final)


        # Return
        return final

    def ifinoctets(self):
        """Return dict of IFMIB ifInOctets for each ifIndex for device.

        Args:
            None

        Returns:
            result: List of ifInOctets DataPoint objects

        """
        # Process OID
        oid = '.1.3.6.1.2.1.2.2.1.10'
        result = self._query.walk(oid)
        return result

    def ifoutoctets(self):
        """Return dict of IFMIB ifOutOctets for each ifIndex for device.

        Args:
            None

        Returns:
            result: List of ifOutOctets DataPoint objects

        """
        # Process OID
        oid = '.1.3.6.1.2.1.2.2.1.16'
        result = self._query.walk(oid)
        return result

    def ifdescr(self):
        """Return dict of IFMIB ifDescr for each ifIndex for device.

        Args:
            None

        Returns:
            result: List of ifDescr DataPoint objects

        """
        # Process OID
        oid = '.1.3.6.1.2.1.2.2.1.2'
        result = self._query.walk(oid)
        return result

    def ifalias(self):
        """Return dict of IFMIB ifAlias for each ifIndex for device.

        Args:

        Returns:
            result: List of ifAlias DataPoint objects

        """
        # Process OID
        oid = '.1.3.6.1.2.1.31.1.1.1.18'
        result = self._query.walk(oid)
        return result

    def ifname(self):
        """Return dict of IFMIB ifName for each ifIndex for device.

        Args:
            None

        Returns:
            result: List of ifName DataPoint objects

        """
        # Process OID
        oid = '.1.3.6.1.2.1.31.1.1.1.1'
        result = self._query.walk(oid)
        return result

    def ifindex(self):
        """Return dict of IFMIB ifindex for each ifIndex for device.

        Args:
            None

        Returns:
            result: List of ifindex DataPoint objects

        """
        # Process OID
        oid = '.1.3.6.1.2.1.2.2.1.1'
        result = self._query.walk(oid)
        return result

    def ifinmulticastpkts(self):
        """Return dict of IFMIB ifInMulticastPkts for each ifIndex for device.

        Args:
            None

        Returns:
            result: List of ifInMulticastPkts DataPoint objects

        """
        # Process OID
        oid = '.1.3.6.1.2.1.31.1.1.1.2'
        result = self._query.walk(oid)
        return result

    def ifoutmulticastpkts(self):
        """Return dict of IFMIB ifOutMulticastPkts for each ifIndex for device.

        Args:
            None

        Returns:
            result: List of ifOutMulticastPkts DataPoint objects

        """
        # Process OID
        oid = '.1.3.6.1.2.1.31.1.1.1.4'
        result = self._query.walk(oid)
        return result

    def ifinbroadcastpkts(self):
        """Return dict of IFMIB ifInBroadcastPkts for each ifIndex for device.

        Args:
            None

        Returns:
            result: List of ifInBroadcastPkts DataPoint objects

        """
        # Process OID
        oid = '.1.3.6.1.2.1.31.1.1.1.3'
        result = self._query.walk(oid)
        return result

    def ifoutbroadcastpkts(self):
        """Return dict of IFMIB ifOutBroadcastPkts for each ifIndex for device.

        Args:
            None

        Returns:
            result: List of ifOutBroadcastPkts DataPoint objects

        """
        # Process OID
        oid = '.1.3.6.1.2.1.31.1.1.1.5'
        result = self._query.walk(oid)
        return result

    def ifhcinucastpkts(self):
        """Return dict of IFMIB ifHCInUcastPkts for each ifIndex for device.

        Args:
            None

        Returns:
            data_dict: Dict of ifHCInUcastPkts using the oid's last node as key

        """
        # Process OID
        oid = '.1.3.6.1.2.1.31.1.1.1.7'
        result = self._query.walk(oid)
        return result

    def ifhcoutucastpkts(self):
        """Return dict of IFMIB ifHCOutUcastPkts for each ifIndex for device.

        Args:
            None

        Returns:
            data_dict: Dict of ifHCOutUcastPkts. Key = OID's last node.

        """
        # Process OID
        oid = '.1.3.6.1.2.1.31.1.1.1.11'
        result = self._query.walk(oid)
        return result

    def ifhcinmulticastpkts(self):
        """Return dict IFMIB ifHCInMulticastPkts for each ifIndex for device.

        Args:
            None

        Returns:
            data_dict: Dict of ifHCInMulticastPkts. Key = OID's last node.

        """
        # Process OID
        oid = '.1.3.6.1.2.1.31.1.1.1.8'
        result = self._query.walk(oid)
        return result

    def ifhcoutmulticastpkts(self):
        """Return dict IFMIB ifHCOutMulticastPkts for each ifIndex for device.

        Args:
            None

        Returns:
            data_dict: Dict of ifHCOutMulticastPkts. Key = OID's last node.

        """
        # Process OID
        oid = '.1.3.6.1.2.1.31.1.1.1.12'
        result = self._query.walk(oid)
        return result

    def ifhcinbroadcastpkts(self):
        """Return dict IFMIB ifHCInBroadcastPkts for each ifIndex for device.

        Args:
            None

        Returns:
            data_dict: Dict of ifHCInBroadcastPkts. Key = OID's last node.

        """
        # Process OID
        oid = '.1.3.6.1.2.1.31.1.1.1.9'
        result = self._query.walk(oid)
        return result

    def ifhcoutbroadcastpkts(self):
        """Return dict IFMIB ifHCOutBroadcastPkts for each ifIndex for device.

        Args:
            None

        Returns:
            data_dict: Dict of ifHCOutBroadcastPkts. Key = OID's last node.

        """
        # Process OID
        oid = '.1.3.6.1.2.1.31.1.1.1.13'
        result = self._query.walk(oid)
        return result

    def ifhcinoctets(self):
        """Return dict of IFMIB ifHCInOctets for each ifIndex for device.

        Args:
            None

        Returns:
            data_dict: Dict of ifHCInOctets. Key = OID's last node.

        """
        # Process OID
        oid = '.1.3.6.1.2.1.31.1.1.1.6'
        result = self._query.walk(oid)
        return result

    def ifhcoutoctets(self):
        """Return dict of IFMIB ifHCOutOctets for each ifIndex for device.

        Args:
            None

        Returns:
            data_dict: Dict of ifHCOutOctets. Key = OID's last node.

        """
        # Process OID
        oid = '.1.3.6.1.2.1.31.1.1.1.10'
        result = self._query.walk(oid)
        return result


def _get_data(title, func, dest):
    """Populate dest with data from the given function.

    Args:
        title: The name of the data
        func: The function which will return the data
        dest: a dict which will store the data

    Returns:
        dest: The modified destination dict

    """
    # Get interface data
    dest[title] = func()
    return dest
