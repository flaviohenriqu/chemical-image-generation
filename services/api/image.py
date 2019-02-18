# services/api/image.py
import cairosvg
import connexion
import flask
import os

from datetime import datetime
from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem.Draw import DrawingOptions

from flask import jsonify
from flask import send_file


DrawingOptions.atomLabelFontSize = 55
DrawingOptions.dotsPerAngstrom = 100
DrawingOptions.bondLineWidth = 3.0


def ping_pong():
    return jsonify({
        'success': True,
        'message': 'ping pong!'
    })


def get_image(image_type):
    try:
        file_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), '..', 'files')
        )
        smiles = flask.request.headers['Smiles']
        mol = Chem.MolFromSmiles(smiles)
        _name = datetime.now().strftime('%Y%m%d-%H%M%S%f')
        temp_filename = '%s/temp/temp_%s.svg' % (file_path, _name)
        _filename = '%s/image_%s.png' % (file_path, _name)
        Draw.MolToFile(mol, temp_filename, size=(800, 600))
        if image_type == 'png':
            cairosvg.svg2png(url=temp_filename, write_to=_filename)
        else:
            _filename = temp_filename
    except ValueError:
        return jsonify({
            'success': False, 'message': 'Null molecule provided'
        }), 400

    return send_file(_filename)

