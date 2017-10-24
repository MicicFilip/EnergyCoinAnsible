from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

def get_rpc_connection():
    """
    Returns the RPC connection to the GAME client
    """
    return AuthServiceProxy("http://%s:%s@127.0.0.1:%s" % ('rpcenergyuser',
                                                           'rpcenergypassword',
                                                           22706))


def get_block_count():
    rpc_connection = get_rpc_connection()

    get_number_of_blocks = rpc_connection.getblockcount()

    # return get_number_of_blocks
    print get_number_of_blocks

if __name__ == "__main__":
    get_block_count()