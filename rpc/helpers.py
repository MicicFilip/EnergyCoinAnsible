from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

def get_rpc_connection():
    """
    Returns the RPC connection to the GAME client
    """
    return AuthServiceProxy("http://%s:%s@127.0.0.1:%s" % ('rpcenergyuser',
                                                           'rpcenergypassword',
                                                           22706))

