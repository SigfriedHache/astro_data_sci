from astropy.coordinates import SkyCoord


def make_rectangle(x1, x2, y1, y2):
    """Return the corners of a rectangle."""
    xs = [x1, x1, x2, x2, x1]
    ys = [y1, y2, y2, y1, y1]
    return xs, ys


def make_sky_rectangle(x1, x2, y1, y2, frame):
    """Return the SkyCoords of a rectangle."""
    phi1s, phi2s = make_rectangle(x1, x2, y1, y2)
    return SkyCoord(phi1s, phi2s, frame=frame)
