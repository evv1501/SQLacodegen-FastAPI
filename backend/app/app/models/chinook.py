# coding: utf-8
from sqlalchemy import Column, DateTime, ForeignKey, Integer, Numeric, String, Table
from sqlalchemy.orm import relationship

from app.db.base_class import Base

metadata = Base.metadata

class Artist(Base):
    __tablename__ = 'Artist'

    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String(120))


class Employee(Base):
    __tablename__ = 'Employee'

    EmployeeId = Column(Integer, primary_key=True)
    LastName = Column(String(20), nullable=False)
    FirstName = Column(String(20), nullable=False)
    Title = Column(String(30))
    ReportsTo = Column(ForeignKey('Employee.EmployeeId'), index=True)
    BirthDate = Column(DateTime)
    HireDate = Column(DateTime)
    Address = Column(String(70))
    City = Column(String(40))
    State = Column(String(40))
    Country = Column(String(40))
    PostalCode = Column(String(10))
    Phone = Column(String(24))
    Fax = Column(String(24))
    Email = Column(String(60))

    parent = relationship('Employee', remote_side=[EmployeeId])


class Genre(Base):
    __tablename__ = 'Genre'

    GenreId = Column(Integer, primary_key=True)
    Name = Column(String(120))


class MediaType(Base):
    __tablename__ = 'MediaType'

    MediaTypeId = Column(Integer, primary_key=True)
    Name = Column(String(120))


class Playlist(Base):
    __tablename__ = 'Playlist'

    PlaylistId = Column(Integer, primary_key=True)
    Name = Column(String(120))

    Track = relationship('Track', secondary='PlaylistTrack')


class Album(Base):
    __tablename__ = 'Album'

    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String(160), nullable=False)
    ArtistId = Column(ForeignKey('Artist.ArtistId'), nullable=False, index=True)

    Artist = relationship('Artist')


class Customer(Base):
    __tablename__ = 'Customer'

    CustomerId = Column(Integer, primary_key=True)
    FirstName = Column(String(40), nullable=False)
    LastName = Column(String(20), nullable=False)
    Company = Column(String(80))
    Address = Column(String(70))
    City = Column(String(40))
    State = Column(String(40))
    Country = Column(String(40))
    PostalCode = Column(String(10))
    Phone = Column(String(24))
    Fax = Column(String(24))
    Email = Column(String(60), nullable=False)
    SupportRepId = Column(ForeignKey('Employee.EmployeeId'), index=True)

    Employee = relationship('Employee')


class Invoice(Base):
    __tablename__ = 'Invoice'

    InvoiceId = Column(Integer, primary_key=True)
    CustomerId = Column(ForeignKey('Customer.CustomerId'), nullable=False, index=True)
    InvoiceDate = Column(DateTime, nullable=False)
    BillingAddress = Column(String(70))
    BillingCity = Column(String(40))
    BillingState = Column(String(40))
    BillingCountry = Column(String(40))
    BillingPostalCode = Column(String(10))
    Total = Column(Numeric(10, 2), nullable=False)

    Customer = relationship('Customer')


class Track(Base):
    __tablename__ = 'Track'

    TrackId = Column(Integer, primary_key=True)
    Name = Column(String(200), nullable=False)
    AlbumId = Column(ForeignKey('Album.AlbumId'), index=True)
    MediaTypeId = Column(ForeignKey('MediaType.MediaTypeId'), nullable=False, index=True)
    GenreId = Column(ForeignKey('Genre.GenreId'), index=True)
    Composer = Column(String(220))
    Milliseconds = Column(Integer, nullable=False)
    Bytes = Column(Integer)
    UnitPrice = Column(Numeric(10, 2), nullable=False)

    Album = relationship('Album')
    Genre = relationship('Genre')
    MediaType = relationship('MediaType')


class InvoiceLine(Base):
    __tablename__ = 'InvoiceLine'

    InvoiceLineId = Column(Integer, primary_key=True)
    InvoiceId = Column(ForeignKey('Invoice.InvoiceId'), nullable=False, index=True)
    TrackId = Column(ForeignKey('Track.TrackId'), nullable=False, index=True)
    UnitPrice = Column(Numeric(10, 2), nullable=False)
    Quantity = Column(Integer, nullable=False)

    Invoice = relationship('Invoice')
    Track = relationship('Track')


t_PlaylistTrack = Table(
    'PlaylistTrack', metadata,
    Column('PlaylistId', ForeignKey('Playlist.PlaylistId'), primary_key=True, nullable=False),
    Column('TrackId', ForeignKey('Track.TrackId'), primary_key=True, nullable=False, index=True)
)
