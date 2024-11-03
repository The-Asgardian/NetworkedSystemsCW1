# Part 3 of Coursework 1
# based on Project 1 from UW's CSEP-561

from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()


class Firewall(object):
    """
    A Firewall object is created for each switch that connects.
    A Connection object for that switch is passed to the __init__ function.
    """

    def __init__(self, connection):
        
        self.connection = connection
        connection.addListeners(self)
        self.setup_firewall_rules()

    def setup_firewall_rules(self):
        # Allow ICMP (ping) traffic
        icmp_rule = of.ofp_flow_mod()
        icmp_rule.match.dl_type = 0x0800  
        icmp_rule.match.nw_proto = 1      
        icmp_rule.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
        self.connection.send(icmp_rule)

        # Allow ARP traffic
        arp_rule = of.ofp_flow_mod()
        arp_rule.match.dl_type = 0x0806 
        arp_rule.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
        self.connection.send(arp_rule)

        # Drop any other traffic
        drop_rule = of.ofp_flow_mod()
        drop_rule.priority = 1            
        self.connection.send(drop_rule)

    def _handle_PacketIn(self, event):
        """
        Packets not handled by the firewall rules will be
        forwarded to this method to be handled by the controller
        """
        packet = event.parsed  # This is the parsed packet data.
        if not packet.parsed:
            log.warning("Ignoring incomplete packet")
            return

        log.info("Unhandled packet from %s: %s" % (packet.src, packet.dump()))


def launch():
    """
    Starts the component
    """

    def start_switch(event):
        log.debug("Controlling %s" % (event.connection,))
        Firewall(event.connection)

    core.openflow.addListenerByName("ConnectionUp", start_switch)
