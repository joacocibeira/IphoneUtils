import pytest
from rest_framework.reverse import reverse
from shortcuts.api.api import ClipboardQueueAPIView
from shortcuts.models import ClipboardQueue
from rest_framework import status


@pytest.mark.django_db
def test_copy_with_empty_queue(api_client, auth_user):
    url = reverse('clipboard-queue')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['item'] == None

@pytest.mark.django_db
def test_copy(api_client, auth_user):
    ClipboardQueue.objects.create(user=auth_user, item='test_item_get')
    url = reverse('clipboard-queue')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['item'] == 'test_item_get'
    item = ClipboardQueue.objects.first()
    assert item == None # The copied item should be deleted from the queue


@pytest.mark.django_db
def test_paste(api_client):
    url = reverse('clipboard-queue')
    payload = {
        'item': 'test_item_post'
    }
    response = api_client.post(url, payload)
    item = ClipboardQueue.objects.first()
    assert response.status_code == status.HTTP_201_CREATED
    assert item.item == 'test_item_post'
