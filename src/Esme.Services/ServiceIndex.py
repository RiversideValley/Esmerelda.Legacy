from Flux import stx

class Service(object):
    def __init__(service, name, bundle, desc, stage, dir):
        service.name = name
        service.bundle = bundle
        service.desc = desc
        service.stage = stage
        service.dir = dir

# location = Service("Location", "Esme.Services.Location", "Helps you locate using the Global Positioning System", 0.1, "Location" )