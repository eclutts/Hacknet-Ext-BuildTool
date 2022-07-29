# reads out the database.

from configparser import ConfigParser

import psycopg
from config import config
from node import node
from eosdevice import eosdevice
from eosnote import eosnote
from eosmail import eosmail
from encrypted_file import encrypted_file
import memory_dump_file
import mem_dump_gen
import account
import dlink
import position_near as pn
import file

def get_all():
    """ Connect to PostgreSQL database server """
    conn = None
    node_get = "SELECT * FROM nodes"
    obj_get = """SELECT * FROM %s e
WHERE e.init_id = '%s'::UUID"""
    
    node_get_specific = "SELECT %s FROM %s WHERE %s.sql_id = '%s'::UUID"
    
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg.connect(**params)
		
        # create a cursor
        cur = conn.cursor()

        cur.execute(node_get)

        row = cur.fetchone()

        while row is not None:
            # this is where we open an xml file.
            sql_id = row[0]
            test = node(*row)


            cur_acc = conn.cursor()
            cur_acc.execute(obj_get % ('accounts', sql_id))
            row_acc = cur_acc.fetchone()
            while row_acc is not None:
                test.add_reference(account.account(*row_acc))
                row_acc = cur_acc.fetchone()
            cur_acc.close()

            cur_dlink = conn.cursor()
            cur_dlink.execute(obj_get % ('dlink', sql_id))
            row_dlink = cur_dlink.fetchone()
            while row_dlink is not None:
                cur_dlink_target = conn.cursor()
                dlink_sql_id = row_dlink[2]
                cur_dlink_target.execute(node_get_specific % ('nodes.id', 'nodes', 'nodes', dlink_sql_id))
                row_dlink_target = cur_dlink_target.fetchone()
                if row_dlink_target is None:
                    cur_dlink_target.execute(node_get_specific % ('eosdevice.id', 'eosdevice', 'eosdevice', dlink_sql_id))
                    row_dlink_target = cur_dlink_target.fetchone()
                test.add_reference(dlink.dlink(*row_dlink_target))
                cur_dlink_target.close()
                row_dlink = cur_dlink.fetchone()
            
            
            cur_dlink.execute(obj_get % ('positionnear', sql_id))
            row_dlink = cur_dlink.fetchone()
            while row_dlink is not None:
                cur_dlink_target = conn.cursor()
                dlink_sql_id = row_dlink[2]
                cur_dlink_target.execute(node_get_specific % ('nodes.id', 'nodes', 'nodes', dlink_sql_id))
                row_dlink_target = cur_dlink_target.fetchone()
                if row_dlink_target is None:
                    cur_dlink_target.execute(node_get_specific % ('eosdevice.id', 'eosdevice', 'eosdevice', dlink_sql_id))
                    row_dlink_target = cur_dlink_target.fetchone()
                test.add_reference(pn.position_near(*row_dlink, *row_dlink_target))
                cur_dlink_target.close()
                row_dlink = cur_dlink.fetchone()
            cur_dlink.close()

            cur_file = conn.cursor()
            cur_file.execute(obj_get % ('files', sql_id))
            row_file = cur_file.fetchone()

            while row_file is not None:
                test.add_reference(file.file(*row_file))
                row_file = cur_file.fetchone()
            cur_file.close()

            cur_enc = conn.cursor()
            cur_enc.execute(obj_get % ('encryptedfiles', sql_id))
            row_enc = cur_enc.fetchone()
            while row_enc is not None:
                if row_enc[5] is not None:
                    cur_enc_ip = conn.cursor()
                    cur_enc_ip.execute(node_get_specific % ('ip', 'nodes', 'nodes', sql_id))
                    row_enc_ip = cur_enc_ip.fetchone()
                    test.add_reference(encrypted_file(*row_enc, *row_enc_ip))
                    cur_enc_ip.close()
                else:
                    test.add_reference(encrypted_file(*row_enc))
                row_enc = cur_enc.fetchone()
            cur_enc.close()

            cur_memf = conn.cursor()
            cur_memf.execute(obj_get % ('memorydumpfiles', sql_id))
            row_memf = cur_memf.fetchone()
            while row_memf is not None:
                
                test.add_reference(memory_dump_file.memory_dump_file(*row_memf))
                row_memf = cur_memf.fetchone()
            cur_memf.close()


            cur_memd = conn.cursor()
            cur_memd.execute(obj_get % ('memorydumpgen', sql_id))
            row_memd = cur_memd.fetchone()
            while row_memd is not None:
                test.add_reference(mem_dump_gen.mem_dump_gen(*row_memd))
                row_memd = cur_memd.fetchone()

            



            cur_eos = conn.cursor()
            cur_eos.execute(obj_get % ('eosdevice', sql_id))
            row_eos = cur_eos.fetchone()
            
            while row_eos is not None:
                eos_sql_id = row_eos[0]
                phone = eosdevice(*row_eos)
                test.add_reference(phone)
                cur_eos_note = conn.cursor()
                
                cur_eos_note.execute(obj_get % ('eosnotes', eos_sql_id))
                
                row_eos_note = cur_eos_note.fetchone()
                while row_eos_note is not None:
                    note = eosnote(*row_eos_note)
                    phone.add_reference(note)
                    row_eos_note = cur_eos_note.fetchone()
                cur_eos_note.close()

                cur_eos_mail = conn.cursor()
                cur_eos_mail.execute(obj_get % ('eosmail', eos_sql_id))
                row_eos_mail = cur_eos_mail.fetchone()
                while row_eos_mail is not None:
                    mail = eosmail(*row_eos_mail)
                    phone.add_reference(mail)
                    row_eos_mail = cur_eos_mail.fetchone()
                cur_eos_mail.close()
                row_eos = cur_eos.fetchone()
                # to be added: everything else for files and whatnot.
                
            cur_eos.close()
            f = open("%s_%s.xml" % (row[1], row[2]), "w")
            for i in test.xml_file_gen():
                f.write(i + "\n")
            print('\n'.join(test.xml_file_gen()))
            row = cur.fetchone()

        cur.close()



    except (Exception, psycopg.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()




if __name__ == '__main__':
    get_all()
    
