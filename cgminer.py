'''
Saltstack for cgminer API
'''

import time
import salt.utils
try:
    import pycgminer
    def make_cmd(name):
        def _cmd(*args, **kwargs):
            return cmd(name, *args, **kwargs)
        return _cmd
except ImportError:
    def make_cmd(name):
        def _cmd(*args, **kwargs):
            return {
                'STATUS': {
                    'Code': -1,
                    'Description': 'pycgminer not installed',
                    'Msg': 'Run pip install pycgminer and restart minion',
                    'STATUS': 'E',
                    'When': int(time.time())
                }
            }
        return _cmd

requests = [
    'version','config','summary','pools','devs','gpu','pga','gpucount','pgacount',
    'switchpool','enablepool','addpool','poolpriority','poolquota','disablepool',
    'removepool','gpuenable','gpudisable','gpurestart','gpuintensity','gpumem',
    'gpuengine','gpufan','gpuvddc','save','quit','notify','privileged','pgaenable',
    'pgadisable','pgaidentify','devdetails','restart','stats','check','failover-only',
    'coin','debug','setconfig','usbstats','pgaset','zero','hotplug','asc','ascenable',
    'ascdisable','ascidentify','asccount','ascset','lockstats','version','config',
    'summary','pools','devs','gpu','pga','gpucount','pgacount','switchpool','enablepool',
    'addpool','poolpriority','poolquota','disablepool','removepool','gpuenable',
    'gpudisable','gpurestart','gpuintensity','gpumem','gpuengine','gpufan','gpuvddc',
    'save','quit','notify','privileged','pgaenable','pgadisable','pgaidentify','devdetails',
    'restart','stats','check','failover-only','coin','debug','setconfig','usbstats','pgaset',
    'zero','hotplug','asc','ascenable','ascdisable','ascidentifyasccount','ascset','lockstats'
]

def cmd(request, *args, **kwargs):
    '''
    Return the result of a cgminer request to port 4028 on localhost

    CLI Example::

        salt '*' cgminer.pools
        salt 'aurum' gpufan 0,80
    '''
    api = pycgminer.CgminerAPI()
    result = api.command(request, *args)
    return result

'''
Create saltstack commands
'''
for request in requests:
    globals()[request] = make_cmd(request)

