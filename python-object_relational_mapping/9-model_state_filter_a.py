if __name__ == "__main__":
    
    '''importing from sys, model_state and sqlalchely'''
    from sys import argv
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    
    path = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(path.format(argv[1], argv[2], argv[3]))
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    for states in session.query(State).filter(State.name.like('%a%')).order_by(State.id).all():
        print("{}: {}".format(states.id, states.name))

        
    session.close()