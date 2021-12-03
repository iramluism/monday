from monday.resources.base import BaseResource
from monday.query_joins import get_boards_query, get_boards_by_id_query, get_board_items_query, \
    get_columns_by_board_query, create_board_query


class BoardResource(BaseResource):

    KIND_PUBLIC = "public"
    KIND_PRIVATE = "private"
    KIND_SHARE = "share"

    def __init__(self, token):
        super().__init__(token)

    def create_board(self, name, board_kind, **kwargs):
        query = create_board_query(name, board_kind, **kwargs)
        return self.client.execute(query)

    def fetch_boards(self, **kwargs):
        query = get_boards_query(**kwargs)
        return self.client.execute(query)

    def fetch_boards_by_id(self, board_ids):
        query = get_boards_by_id_query(board_ids)
        return self.client.execute(query)

    def fetch_items_by_board_id(self, board_ids):
        query = get_board_items_query(board_ids)
        return self.client.execute(query)

    def fetch_columns_by_board_id(self, board_ids):
        query = get_columns_by_board_query(board_ids)
        return self.client.execute(query)
