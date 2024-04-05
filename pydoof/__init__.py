token = None
_dfmaster_token = None

management_url = None
search_url = None


def _get_suggestions_index(name):
    """Returns suggestions index name for a regular index name."""
    return f'df_suggestions_{name}'



