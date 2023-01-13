from flask import request
from flask_restx import Resource, Namespace

from dao.model.genre import GenreSchema
from decorators import auth_required, admin_required
from implemented import genre_service

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    @auth_required
    def get(self):
        page = request.args.get("page")

        filters = {
            "page": page,
        }
        rs = genre_service.get_all(filters)
        res = GenreSchema(many=True).dump(rs)
        return res, 200

    @admin_required
    def post(self):
        request_json = request.json
        genre = genre_service.create(request_json)
        return "", 201, {"location": f"/genres/{genre.id}"}

@genre_ns.route('/<int:rid>')
class GenreView(Resource):
    @auth_required
    def get(self, rid):
        r = genre_service.get_one(rid)
        sm_d = GenreSchema().dump(r)
        return sm_d, 200

    @admin_required
    def put(self, rid):
        request_json = request.json
        if "id" not in request:
            request_json["id"] = rid
        genre_service.update(request_json)
        return "", 204

    @admin_required
    def delete(self, rid):
        genre_service.delete(rid)
        return "", 204
