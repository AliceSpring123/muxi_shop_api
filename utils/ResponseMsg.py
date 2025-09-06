from django.http import HttpResponse


class MenuResponse():

    @staticmethod
    def success(data):
        result = {"status":1000,"data":data}
        return HttpResponse(json.dumps(result), content_type = "application/json")

    @staticmethod
    def failed(data):
        result = {"status": 1001, "data": data}
        return HttpResponse(json.dumps(result), content_type="application/json")

    @staticmethod
    def other(data):
        result = {"status": 1002, "data": data}
        return HttpResponse(json.dumps(result), content_type="application/json")