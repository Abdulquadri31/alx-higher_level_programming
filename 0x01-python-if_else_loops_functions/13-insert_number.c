#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly linked list.
 * @head: Double pointer to the head of the linked list.
 * @number: The number to insert into the list.
 *
 * Return: The address of the new node, or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new_node, *current;

    new_node = malloc(sizeof(listint_t));
    if (new_node == NULL)
        return (NULL);

    new_node->n = number;

    /* If the list is empty or the new node should be inserted at the head */
    if (*head == NULL || (*head)->n >= number)
    {
        new_node->next = *head;
        *head = new_node;
        return (new_node);
    }

    current = *head;
    
    /* Traverse the list to find the correct insertion point */
    while (current->next != NULL && current->next->n < number)
        current = current->next;

    new_node->next = current->next;
    current->next = new_node;

    return (new_node);
}