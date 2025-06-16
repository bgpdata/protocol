package org.bgpdata.api.parsed.message;

import java.io.Serializable;

/**
 * POJO for Subscription messages from the web client.
 * <p>
 * This class is not like the others from the collector; it's a client-side
 * message, so it has a much simpler format.
 * <p>
 * Format: action\tasn
 */
public class Subscription implements Serializable {
    private String action;
    private String resource;

    public Subscription(String value) {
        if (value == null || value.isEmpty()) {
            throw new IllegalArgumentException("Subscription message cannot be null or empty.");
        }

        String[] parts = value.split("\t");

        if (parts.length >= 2) {
            this.action = parts[0];
            try {
                this.resource = parts[1].trim();
            } catch (Exception e) {
                throw new IllegalArgumentException("Invalid resource format in subscription message: " + value, e);
            }
        } else {
            throw new IllegalArgumentException("Invalid subscription message format: " + value);
        }
    }

    public String getAction() {
        return action;
    }

    public String getResource() {
        return resource;
    }
} 