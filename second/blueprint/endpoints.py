from common import create_histogram, timed
from second.blueprint import api
from second.service.httpbin import make_request


_histogram = create_histogram(
    name="httpbin.latency",
    unit="1.0",
    description="Track the time taken by the /delay endpoint."
)


@api.post("/")
def post() -> dict:
    with timed(_histogram):
        return make_request()  # Makes a call to HTTPBin
