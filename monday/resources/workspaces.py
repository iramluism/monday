
from monday.resources.base import BaseResource
from monday.query_joins import (
    mutate_workspace_query, add_user_to_workspace_query,
    delete_user_to_workspace_query, get_workspaces_query
)


class WorkspaceResource(BaseResource):

    KIND_OPEN = "open"
    KIND_CLOSED = "closed"

    SUBSCRIBER = "subscriber"
    OWNER = "owner"

    def __init__(self, token):
        super().__init__(token)

    def create_workspace(self, name, kind=None, description=None):
        kind = kind or self.KIND_OPEN
        query = mutate_workspace_query(name, kind, description)
        return self.client.execute(query)

    def fetch_workspace(self, board_ids=None):
        query = get_workspaces_query(board_ids)
        return self.client.execute(query)

    def add_user_to_workspace(self, workspace_id, user_ids, kind):
        query = add_user_to_workspace_query(workspace_id, user_ids, kind)
        return self.client.execute(query)

    def delete_user_to_workspace(self, workspace_id, user_ids):
        query = delete_user_to_workspace_query(workspace_id, user_ids)
        return self.client.execute(query)
