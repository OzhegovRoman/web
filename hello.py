def app(env, start_response):
	start_response('200 OK', [('Content-Type', 'text/plain')])
	query = ""
	for (key,value) in env.iteritems():
		if key == "QUERY_STRING":
			 query = value
	return query.replace('&','\n')
