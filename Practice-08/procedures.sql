
CREATE TABLE IF NOT EXISTS contacts (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE,
    phone TEXT
);

CREATE OR REPLACE PROCEDURE insert_user(p_name TEXT, p_phone TEXT)
LANGUAGE plpgsql AS $$
BEGIN
    INSERT INTO contacts(name, phone) VALUES (p_name, p_phone);
END;
$$;

CREATE OR REPLACE PROCEDURE update_user(p_name TEXT, p_phone TEXT)
LANGUAGE plpgsql AS $$
BEGIN
    UPDATE contacts SET phone = p_phone WHERE name = p_name;
END;
$$;

CREATE OR REPLACE PROCEDURE delete_user(p TEXT)
LANGUAGE plpgsql AS $$
BEGIN
    DELETE FROM contacts WHERE name = p OR phone = p;
END;
$$;
