class Variables():
    def create_workspace_variable(self, workspace_id, key, value, category='terraform', hcl=False, sensitive=False):
        url = self.url + 'vars'
        payload = {
            "data": {
                "type": "vars",
                "attributes": {
                    "key": key,
                    "value": value,
                    "category": category,
                    "hcl": hcl,
                    "sensitive": sensitive
                },
                "relationships": {
                    "workspace": {
                        "data": {
                            "id": workspace_id,
                            "type": "workspaces"
                        }
                    }
                }
            }
        }
        return self._post_handler(url=url, json=payload)

    def list_variables(self, organization, workspace):
        url = self.url + 'vars?filter%5Borganization%5D%5Bname%5D={}&filter%5Bworkspace%5D%5Bname%5D={}'\
            .format(organization, workspace)
        return self._get_handler(url)

    def delete_workspace_variable(self, variable_id):
        url = self.url + '/vars/{}'.format(variable_id)
        return self._delete_handler(url)
