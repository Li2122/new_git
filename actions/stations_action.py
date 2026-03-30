from actions.object_api import RestApi
from data.config import RestEndpoints
from models.get_stations_response import Stations


class StationsActions(RestApi):

    def get_stations(self):
        response = self.get(RestEndpoints.stations)
        list_stations = []
        for station in response.json():
            list_stations.append(Stations(**station))
        return list_stations