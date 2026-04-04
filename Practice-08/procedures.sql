CREATE OR REPLACE PROCEDURE upsert_user(p_name VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM contacts WHERE name = p_name) THEN
        UPDATE contacts SET phone = p_phone WHERE name = p_name;
    ELSE
        INSERT INTO contacts(name, phone) VALUES (p_name, p_phone);
    END IF;
END;
$$;

CREATE OR REPLACE PROCEDURE insert_many(names text[], phones text[])
LANGUAGE plpgsql AS $$
DECLARE
    i int := 1;
BEGIN
    WHILE i <= array_length(names, 1) LOOP
        IF phones[i] ~ '^[0-9]+$' THEN
            CALL upsert_user(names[i], phones[i]);
        END IF;
        i := i + 1;
    END LOOP;
END;
$$;

CREATE OR REPLACE PROCEDURE delete_user(p text)
LANGUAGE plpgsql AS $$
BEGIN
    DELETE FROM contacts
    WHERE name = p OR phone = p;
END;
$$;
