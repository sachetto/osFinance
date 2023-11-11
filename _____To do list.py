# To do list


# This is an example what I need to do:

# Replace "section" by the Category_Repository
def select_category_and_create_asset(category_name):
    category = session.query(Category).filter_by(Category=category_name).first()
    if category is None:
        # Handle the case if the category doesn't exist
        return None

    asset = Asset(
        Symbol="ABC",
        Company_Name="ABC Company",
        Current_Price=10.0,
        Category=category
    )

    session.add(asset)
    session.commit()

    return asset
