from pyramid.view import view_config


@view_config(route_name='home', renderer='../templates/home/default.pt')
def my_view(request):
    return {'project': 'Bill Tracker Pro'}
