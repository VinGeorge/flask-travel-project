from flask import Flask, render_template # сперва подключим модуль
import data
app = Flask(__name__) # объявим экземпляр фласка

#Создаем страницы

@app.route('/')
def render_main():


    return render_template("index.html", title=data.title, subtitle=data.subtitle,
                           tours=data.tours, description=data.description, departures=data.departures)

@app.route('/products/')
def render_products():
	return 'Продукты'

@app.route('/about/')
def render_about():
	return 'Информация о проекте'

#Принимаем один параметр
@app.route('/departure/<departure_id>/')
def departure(departure_id):

    local_tours, prices, nights=[], [], []

    for tour in data.tours.values():
        if tour['departure'] == departure_id:
            local_tours.append(tour)
            prices.append(tour['price'])
            nights.append(tour['nights'])

    return render_template("departure.html", title=data.title, departures=data.departures, departure_id=departure_id,
                           tours=local_tours, nights=nights, prices=prices)

#Страница ошибок
@app.errorhandler(404) #тут может быть код любой другой ошибки
def render_not_found(error):
    return "Ничего не нашлось! Вот неудача, отправляйтесь на главную!", 404 #указываем код ответа сервера для поисковика

#Параметр e
@app.errorhandler(500)
def render_server_error(error):
    return "Что-то не так, но мы все починим:\n{}".format(error.original_exception), 500


if __name__ == '__main__':
    app.run() # запустим сервер