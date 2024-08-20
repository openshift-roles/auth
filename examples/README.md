Example playbooks
=========
Here you can find all the example playbooks that demonstrated how this role can be leveraged to configure authentication in Openshift clusters

Pre-Requisites
--------
This role requires api_token to authenticate with cluster as well as the client id and client secret obtained from the oidc auth provider be set in an ansible vault secrets file. Run command below to create this file

```sh
ansible-vault create vars/secrets.yml
```

Login to web console of target openshift cluster to configure OIDC auth and copy the login token and include that in the ansible vault secrets.yml file as shown in snippet below

```yml
api_token: <redacted>
client_id: <redacted>
client_secret: <redacted>
```

Playbooks
---------------------
* [Enable Okta Auth](#enable-okta-auth)


## enable okta auth
Assuming you have completed configuration steps in Okta. 

```sh
export VAULT_SECRET="<redacted>"

ansible-playbook --vault-password-file <(echo "$VAULT_SECRET") enable-okta-auth.yml
```