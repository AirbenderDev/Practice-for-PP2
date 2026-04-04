CREATE OR REPLACE FUNCTION search_contacts(p TEXT)
RETURNS TABLE(name TEXT, phone TEXT) AS $$
BEGIN
    RETURN QUERY
    SELECT c.name::TEXT, c.phone::TEXT
    FROM contacts c
    WHERE c.name ILIKE '%' || p || '%'
    OR c.phone ILIKE '%' || p || '%';
END;
$$ LANGUAGE plpgsql;
CREATE OR REPLACE FUNCTION get_contacts_paginated(lim INT, off INT)
RETURNS TABLE(name TEXT, phone TEXT) AS $$
BEGIN
    RETURN QUERY
    SELECT name, phone FROM contacts
    LIMIT lim OFFSET off;
END;
$$ LANGUAGE plpgsql;
