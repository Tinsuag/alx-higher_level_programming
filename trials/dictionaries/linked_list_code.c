#include <stdio.h>
#include <stdlib.h>

struct node{
    int data;
    struct node *link;
};
struct node* insert_data_index(struct node *head, int input_data, int index)
{
    struct node *temp, *ptr;
    int n = 0;

    ptr = head;
    temp = (struct node *)malloc(sizeof(struct node));
    temp -> data = input_data;
    temp -> link = NULL;
    index--;

    while(index != 1)
    {
        ptr = ptr -> link;
        index--;
    }

    temp -> link = ptr -> link;
    ptr -> link = temp;

    return head;
}
struct node* insert_data_beg(struct node *head, int input_data)
{
    struct  node *temp;

    temp = (struct node *)malloc(sizeof(struct node));
    temp -> data = input_data;
    temp -> link = NULL;
    temp -> link = head;
    head = temp;
    return head;

}
void insert_data(struct node *head, int input_data)
{
    struct node *ptr, *temp;
    ptr = head;
    temp = (struct node *)malloc(sizeof(struct node));

    while(ptr -> link != NULL)
    {
        ptr = ptr -> link;
    }
    
    temp -> data = input_data;
    temp -> link = NULL;
    ptr -> link = temp;
}
void count_of_nodes(struct node *head)
{
    int count = 0;
    if(head == NULL)
        printf("Linked List is empty");
    struct node *ptr = NULL;
    ptr = head;
    while(ptr != NULL)
    {
        count++;
        ptr = ptr -> link;
    }

    printf("%d\n", count);
}

void print_linked_list(struct node *head)
{
    if(head == NULL)
        printf("the list is empty");
    struct node *ptr = NULL;
    ptr = head;
    while(ptr != NULL)
    {
        printf("%d \n", ptr -> data);
        ptr = ptr -> link;
    }
}
int main(){
    struct node *head = malloc(sizeof(struct node));
    head -> data = 45;
    head -> link = NULL;
    
    struct node *current = malloc(sizeof(struct node));
    current -> data = 98;
    current -> link = NULL;
    head -> link = current;
    
    current = malloc(sizeof(struct node));
    current -> data = 3;
    current -> link = NULL;
    head -> link -> link = current;
    

    //count_of_nodes(head);
    print_linked_list(head);
    printf("-----------------------------------------------------\n");

    insert_data(head, 76);
    print_linked_list(head);
    printf("-----------------------------------------------------\n");

    head = insert_data_beg(head, 32);
    print_linked_list(head);
    printf("-----------------------------------------------------\n");

    head = insert_data_index(head, 9812, 3);

    //count_of_nodes(head);
    print_linked_list(head);

    free(head);



    return 0;
}