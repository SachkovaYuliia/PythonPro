# Задача 4: створення веб-сервера, що обслуговує кілька клієнтів одночасно
# Напишіть простий веб-сервер, який може обслуговувати кілька клієнтів одночасно, використовуючи потоки або процеси. Ваша програма повинна відповідати на HTTP-запити клієнтів і відправляти їм текстові повідомлення.

# Підказка: можна використовувати вбудовану бібліотеку http.server.

from http.server import SimpleHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn

class ThreadingHTTPServer(ThreadingMixIn, HTTPServer):
    """Цей сервер обслуговує кожного клієнта в окремому потоці"""


class MyRequestHandler(SimpleHTTPRequestHandler):
    """Створюємо клас обробника запитів"""
    def do_GET(self):
        self.send_response(200)
        
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        
        message = "Привіт!"
        self.wfile.write(message.encode("utf-8"))


def run(server_class=ThreadingHTTPServer, handler_class=MyRequestHandler, port=8080):
    """Основна функція для запуску серверу"""
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Сервер запущено на порту {port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
