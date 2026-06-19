"""Tests for students endpoints"""

import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_check():
    """Test health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_list_students():
    """Test list students endpoint"""
    response = client.get("/api/students/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
