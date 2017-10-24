from helpers import get_rpc_connection

def get_block_count():
    rpc_connection = get_rpc_connection()

    get_number_of_blocks = rpc_connection.getblockcount()

    # return get_number_of_blocks
    print get_number_of_blocks

if __name__ == "__main__":
    get_block_count()