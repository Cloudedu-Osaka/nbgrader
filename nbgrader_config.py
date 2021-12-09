c = get_config()
import os

c.NbGraderAPI.timezone = "JST"

c.Validator.lrs_endpoint = 'http://localhost:8081/data/xAPI'
c.Validator.lrs_key      = '9efbfc629a314c67985176db789ef6093aaff2b8'
c.Validator.lrs_secret   = 'a3abd823e96b283a622167040bbd13e3e33edfa7'

c.Validator.lrs_course_id = 'http://example.com/'

# [jupyterhub/spawners.md at main · jupyterhub/jupyterhub](https://github.com/jupyterhub/jupyterhub/blob/main/docs/source/reference/spawners.md)
c.Validator.lrs_user = os.environ.get('JUPYTERHUB_USER') or 'jovyan'
