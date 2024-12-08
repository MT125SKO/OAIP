import sqlalchemy as sa
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy import create_engine
import datetime


engine = create_engine('sqlite:///data_bd.db', echo=True)
Base = declarative_base()


class Client(Base):
    __tablename__ = 'clients'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String)
    surname = sa.Column(sa.String)
    phone = sa.Column(sa.String)
    email = sa.Column(sa.String)
    orders = relationship("Order", back_populates="client")

    def __repr__(self):
        return f"<Client(name='{self.name}', surname='{self.surname}')>"

class Tour(Base):
    __tablename__ = 'tours'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String)
    description = sa.Column(sa.Text)
    price = sa.Column(sa.Float)
    country = sa.Column(sa.String)
    city = sa.Column(sa.String)
    start_date = sa.Column(sa.Date)
    end_date = sa.Column(sa.Date)
    orders = relationship("Order", back_populates="tour")
    hotels = relationship("Hotel", secondary="tours_hotels", back_populates="tours")

    def __repr__(self):
        return f"<Tour(name='{self.name}', country='{self.country}')>"

class Order(Base):
    __tablename__ = 'orders'
    id = sa.Column(sa.Integer, primary_key=True)
    client_id = sa.Column(sa.Integer, sa.ForeignKey('clients.id'))
    tour_id = sa.Column(sa.Integer, sa.ForeignKey('tours.id'))
    order_date = sa.Column(sa.Date)
    seats_count = sa.Column(sa.Integer)
    client = relationship("Client", back_populates="orders")
    tour = relationship("Tour", back_populates="orders")

    def __repr__(self):
        return f"<Order(client_id={self.client_id}, tour_id={self.tour_id})>"


class Hotel(Base):
    __tablename__ = 'hotels'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String)
    city = sa.Column(sa.String)
    country = sa.Column(sa.String)
    rating = sa.Column(sa.Float)
    tours = relationship("Tour", secondary="tours_hotels", back_populates="hotels")

    def __repr__(self):
        return f"<Hotel(name='{self.name}', city='{self.city}')>"


class ToursHotels(Base):
    __tablename__ = 'tours_hotels'
    tour_id = sa.Column(sa.Integer, sa.ForeignKey('tours.id'), primary_key=True)
    hotel_id = sa.Column(sa.Integer, sa.ForeignKey('hotels.id'), primary_key=True)


# Create tables if they don't exist
try:
    Base.metadata.create_all(engine)
    print("Tables created successfully.")
except Exception as e:
    print(f"Error creating tables: {e}")
    exit(1)  # Exit with an error code


Session = sessionmaker(bind=engine)


def add_data(session):
    try:
        new_client = Client(name="Иван", surname="Иванов", phone="222", email="5445.com")
        new_tour = Tour(name="Тур в z", description="туристический путь", price=1000, country="город 1", city="город 2", start_date=datetime.date(2024, 5, 1), end_date=datetime.date(2024, 5, 10))
        new_hotel = Hotel(name="Отель", city="город", country="Россия", rating=4.5)
        new_order = Order(client=new_client, tour=new_tour, order_date=datetime.date.today(), seats_count=2)


        session.add(new_client)
        session.add(new_tour)
        session.add(new_hotel)
        session.add(new_order)
        session.commit()
        print("Данные успешно добавлены.")

    except Exception as e:
        session.rollback()
        print(f"Ошибка добавления данных: {e}")


# Function to perform queries
def run_queries(session):
    try:
        tours_in_paris = session.query(Tour).filter(Tour.city == "Париж").all()
        print("Туры в Париже:")
        for tour in tours_in_paris:
            print(tour)

        clients_with_orders = session.query(Client, Order).join(Order, Client.id == Order.client_id).all()
        print("\nКлиенты с заказами:")
        for client, order in clients_with_orders:
            print(f"Клиент: {client}, Заказ: {order}")

    except Exception as e:
        print(f"Ошибка выполнения запросов: {e}")
with Session() as session:
    add_data(session)
    run_queries(session)


print("Program finished.")