def http_req(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case _: #default case
            return "Unknown"