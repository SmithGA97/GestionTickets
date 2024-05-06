"""Module Description: This module contains functions and classes related 
to the my_package functionality."""

from .celery import app as gestion_tickets_app

__all__ = ("gestion_tickets_app",)
