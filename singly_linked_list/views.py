from django.shortcuts import render,redirect
from django.http import JsonResponse
from .singlylinkedlist import Node, Singly_linked_list


linkedlist = Singly_linked_list()

def home(request):

    nodes = linkedlist.printlinkedlist()

    return render(request, "result.html", {"nodes": nodes})



def add_node(request):
    if request.method == "POST":
        node_value = request.POST.get("node_value")

        if node_value:
            linkedlist.insertAtend(node_value)

    nodes = linkedlist.printlinkedlist()
    return redirect('home')


def insert_at_beg(request):

    if request.method == "POST":

        node_value = request.POST.get("node_value")

        if node_value:
            linkedlist.insertAtBeg(node_value)

    nodes = linkedlist.printlinkedlist()
    return redirect('home')

def insert_at_mid(request):
    if request.method == "POST":
        node_value = request.POST.get("node_value")
        position = request.POST.get("position")
        if node_value and position:
            linkedlist.insertAtMid(node_value,position)
    nodes = linkedlist.printlinkedlist()
    return redirect('home')

# DELETE NODE
def delete_node(request):

    if request.method == "POST":

        delete_value = request.POST.get("node_value")

        if delete_value:
            linkedlist.deleteLinkedlist(delete_value)

    nodes = linkedlist.printlinkedlist()
    return redirect('home')
    

 
   