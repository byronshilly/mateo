from mateo.app import db
from mateo.models.game import Game



def _get_game(game_id):
    game = Game.query.filter_by(id=game_id).first()
    return game


def _get_game_by_title_and_platform(title, platform):
    game = Game.query.filter_by(title=title, platform=platform).first()
    return game


def _create_game(body):
    game = Game(**body)

    db.session.add(game)
    db.session.commit()

    return game


def _delete_game(game_id):
    game = Game.query.filter_by(id=game_id).first()

    db.session.delete(game)
    db.session.commit()

    return True
