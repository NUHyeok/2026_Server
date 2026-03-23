def parse(data):
    request = data.decode('utf-8')
    request_line = request.split('\r\n')[0]
    path = request_line.split(' ')[1]
    return path

def routing(path):
    if path == '/' or path == '/cv.html':
        filename = 'cv.html'
        content_type = 'text/html'
        is_binary = False
        
    elif path == '/styles.css':
        filename = 'styles.css'
        content_type = 'text/css'
        is_binary = False
        
    elif path == '/profile-photo.png':
        filename = 'profile-photo.png'
        content_type = 'image/png'
        is_binary = True
    
    else:
        return None, None, None
    
    return filename, content_type, is_binary
        
def build_response(is_binary, filename, content_type):
    
    if filename is None:
            response = (
                "HTTP/1.1 404 Not Found\r\n"
                "Content-Type: text/html\r\n"
                "Content-Length: 13\r\n"
                "\r\n"
                "404 Not Found"
            ).encode('utf-8')
            return response
        
        
    if is_binary:
            with open(filename, 'rb') as f:
                body = f.read()
    else: 
            with open(filename, 'r', encoding='utf-8') as f:
                body = f.read().encode('utf-8')
            
    content_length = len(body)
        
    response = (
            "HTTP/1.1 200 OK\r\n"
            f"Content-Type: {content_type}\r\n"
            f"Content-Length: {content_length}\r\n"
            "\r\n"
    ).encode('utf-8') + body
    
    return response
    
    
    
