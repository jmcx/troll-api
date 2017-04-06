import falcon
import json
from serialization import load_pipeline

class ModerationResource:
    def on_get(self, req, resp):
        """Handles GET requests"""

        score = clf.predict_proba([req.params['message']])

        result = {
            'score': str(score[0])
        }

        resp.body = json.dumps(result)

clf = load_pipeline('/Users/manu/Downloads/wiki-detox-light/src/modeling', 'toxicity_linear_char_oh_d')
api = falcon.API()
api.add_route('/moderate', ModerationResource())
