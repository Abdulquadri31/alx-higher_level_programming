#include <stddef.h>  // For size_t
#include <stdlib.h>  // For NULL
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the list
 * Return: 1 if palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow = *head, *fast = *head, *prev = NULL;
    listint_t *second_half, *prev_of_slow = NULL;
    int palindrome = 1;

    if (*head == NULL || (*head)->next == NULL)
        return (1);

    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        prev = slow;
        slow = slow->next;
    }

    if (fast != NULL)
    {
        second_half = slow->next;
        slow->next = NULL;
    }
    else
    {
        second_half = slow;
        prev_of_slow = prev;
    }

    while (second_half != NULL)
    {
        if (second_half->n != prev->n)
        {
            palindrome = 0;
            break;
        }
        second_half = second_half->next;
        prev = prev->next;
    }

    if (palindrome == 1 && prev_of_slow != NULL)
        prev_of_slow->next = NULL;

    return (palindrome);
}
