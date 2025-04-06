#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <linux/if_packet.h>
#include <net/ethernet.h>
#include <arpa/inet.h>

#define BUFFER_SIZE 65536

void print_packet(const unsigned char *buffer, int size) {
    struct ethhdr *eth = (struct ethhdr *)buffer;
    printf("[INFO] Packet captured\n");
    printf("Ethernet Header\n");
    printf("   |-Source Address      : %02X:%02X:%02X:%02X:%02X:%02X\n",
           eth->h_source[0], eth->h_source[1], eth->h_source[2],
           eth->h_source[3], eth->h_source[4], eth->h_source[5]);
    printf("   |-Destination Address : %02X:%02X:%02X:%02X:%02X:%02X\n",
           eth->h_dest[0], eth->h_dest[1], eth->h_dest[2],
           eth->h_dest[3], eth->h_dest[4], eth->h_dest[5]);
}

int main() {
    int socket_raw;
    
    unsigned char *buffer = (unsigned char *)malloc(BUFFER_SIZE);
    if (buffer == NULL) {
        perror("[ERROR] Buffer allocation failed");
        return 1;
    }

    // Create a raw socket
    socket_raw = socket(AF_PACKET, SOCK_RAW, htons(ETH_P_ALL));
    if (socket_raw < 0) {
        perror("[ERROR] Socket creation failed");
        free(buffer);
        return 1;
    }

    printf("[INFO] Raw socket created. Listening for packets...\n");

    while (1) {
        // Receive packets
        ssize_t data_size = recvfrom(socket_raw, buffer, BUFFER_SIZE, 0, NULL, NULL);
        if (data_size < 0) {
            perror("[ERROR] Recvfrom error");
            break;
        }

        // Print packet details
        print_packet(buffer, data_size);
        fflush(stdout);
    }

    close(socket_raw);
    free(buffer);
    return 0;
}