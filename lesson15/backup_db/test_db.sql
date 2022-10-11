PGDMP     3    "            	    z            test_db    14.5    14.5     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    16394    test_db    DATABASE     g   CREATE DATABASE test_db WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'Ukrainian_Ukraine.1251';
    DROP DATABASE test_db;
                postgres    false            �            1259    16410    address    TABLE     X   CREATE TABLE public.address (
    pk_id integer NOT NULL,
    address character(100)
);
    DROP TABLE public.address;
       public         heap    postgres    false            �            1259    16396    ads    TABLE     �   CREATE TABLE public.ads (
    pk_id integer NOT NULL,
    name character(100),
    fk_author integer,
    price numeric,
    description text,
    fk_address integer,
    is_published boolean
);
    DROP TABLE public.ads;
       public         heap    postgres    false            �            1259    16404    author    TABLE     U   CREATE TABLE public.author (
    pk_id integer NOT NULL,
    author character(50)
);
    DROP TABLE public.author;
       public         heap    postgres    false            �          0    16410    address 
   TABLE DATA           1   COPY public.address (pk_id, address) FROM stdin;
    public          postgres    false    211   �       �          0    16396    ads 
   TABLE DATA           c   COPY public.ads (pk_id, name, fk_author, price, description, fk_address, is_published) FROM stdin;
    public          postgres    false    209   �       �          0    16404    author 
   TABLE DATA           /   COPY public.author (pk_id, author) FROM stdin;
    public          postgres    false    210   6       h           2606    16414    address address_pkey 
   CONSTRAINT     U   ALTER TABLE ONLY public.address
    ADD CONSTRAINT address_pkey PRIMARY KEY (pk_id);
 >   ALTER TABLE ONLY public.address DROP CONSTRAINT address_pkey;
       public            postgres    false    211            d           2606    16402    ads ads_pkey 
   CONSTRAINT     M   ALTER TABLE ONLY public.ads
    ADD CONSTRAINT ads_pkey PRIMARY KEY (pk_id);
 6   ALTER TABLE ONLY public.ads DROP CONSTRAINT ads_pkey;
       public            postgres    false    209            f           2606    16408    author author_pkey 
   CONSTRAINT     S   ALTER TABLE ONLY public.author
    ADD CONSTRAINT author_pkey PRIMARY KEY (pk_id);
 <   ALTER TABLE ONLY public.author DROP CONSTRAINT author_pkey;
       public            postgres    false    210            j           2606    16420    ads fk_address    FK CONSTRAINT        ALTER TABLE ONLY public.ads
    ADD CONSTRAINT fk_address FOREIGN KEY (fk_address) REFERENCES public.address(pk_id) NOT VALID;
 8   ALTER TABLE ONLY public.ads DROP CONSTRAINT fk_address;
       public          postgres    false    3176    209    211            i           2606    16415    ads fk_author    FK CONSTRAINT     |   ALTER TABLE ONLY public.ads
    ADD CONSTRAINT fk_author FOREIGN KEY (fk_author) REFERENCES public.author(pk_id) NOT VALID;
 7   ALTER TABLE ONLY public.ads DROP CONSTRAINT fk_author;
       public          postgres    false    210    209    3174            �   �   x���1�@Ek�{ ��i<�B!�&�VM��	���ύ�@,L�Mf�3[�?v���F�(���4jW#�@B����y�j��<�"?H۱S���4d�A�R�9b"��J����b�(�U�Z�~��5{̌JNSL��C�OQ17�-V����B��_f	1���=[J���������T�2מ�����쭫�� ���      �   W  x��Z�n�]S_q���CR�-�.?�M��j	`�#@v$5�hH6!ǚ83��I�-��l���/t�B�`>!uN���8��vؖ�/�ǩ�Suy��}���0��,p��ea�fWy??�"'�e�,v[���6:����q6s�:�gq�OZ.�.��f�#�d�HȺ�������[������e�l%��~p���x��DO�6��d�5e�?�v�:�dI$���݆�M��s�V"�;����Y>�վ�M���@~�e%��E�#n��O�E~t�x��id���+(ťA>v��ۧ��]��8���h�=gt��qI{�0ĭJ��i���������uC���G�[�/}��&��)y�.�u�3���7qԇ�Xr��+F�k:G��&*`_�!�~���P�,��q�Lu�qB ���%�����Ȑ�&��/�gb9��QA�Sh.�3z�He��1Cr��m����t��b\��7S�L�?�$G?;@[�r����
�;=A��L*�=�ע\�RF"C�cH<�H`h /!-��Z�N>,�'��`���c<Ep5a!�]i'��� �8�e�"z_��/�X�P����wLj4����ħ��:?�C��ϡ�+��H�gXo�n���}�}�LXN�E˾�|L(&����� �
3�C�i�v��CE���p���-梃F��EP1N��؊��p��[�6�~,W��_~V`�SZ*�h�L�Z��H/[����%̆8�H[�־V�z���ϊ�1!��	c�׃q��> c䡖�d�N�g����z��ײ���}�>����p_=~�`K��q� x��-\��T�X9"J7v���`d��(�
S�0��I�#F�z��N�( 4���}�Upd�����Y"�Li��:ŀ�vwoߜ�<�Z�蓝�F����k�~�Ba",��mVz5�q�r�=XhIbE�K��ΊsYʫ�ʪ]ǜ
e�\�P���<��xZ`et4��:�OQ5'f��@sH�:�(&C��+��YB>3�z��p��E@���>[��c�R�%�����ׄ�x�4@D�3J3B].6[qzEvds���Ȭ��\�k[X���O�����T���B=vʕH����E�h�ǉ2�H��4"Y3�� ����0��y;��(4�Jp2d�9Cj�'��^��ݢ�Z������D�S��?8���&EB�;�W����$���Lj�ܟ6K�����R�X��#��z�3�CTV>��;HK���u��;��9 �io`����s����gJ���\][ߧ���6vL���mph�K����PUb��(W�QIz%��YC1qL��s͏S2_H>3L��%��Y�Ւ-O�4A�V��
�&�9��
���˄)�����+w-��D�n��������ul�V�Sop}�$(���j]9M���@��hvx���4Z�Y_�#�
S�F�!��z�REf��tG̑v�>S3��8@�H�3(��#toVU�]1��?^���>�~�������y��(?���e,�\�t+Q�kt����\~���?U��_��%�5&h)�c��'����3���!�i��S@r������x}s5`�7�Ŀ�!mC�Zv�����XMc��1�+����zb'Ot�!�kC���VJ�c�Wμ �bt7�� ��ሃ��2ʔ)�����(`�KK���%⣰֮�bl5��m�h�f܅��O
�Ɲ���΢A�){�aQv
�٣��@�m�em�#�z_��Q90��� 4@k�0�Ej@�IΫ|NT�/�0jgٯ�R΂�l#�|��f�u}�>��혛Đ3E� ��b�i}Ҥ�e�_�1�쓑�8�a
���L},V���j��e��Ş��T��t6�Ԁ�|���ǚ�ז|C��V�+lh��_P�4K�Ҷ�猤l�l,L��T1�#�	���x*4Gʚ]���A�:n�Ŋ̠�k6�IJa0�X�	����i�O��N�]����VJC0�9�2�mw�:]]9�L��:g�e(���V�b�2�����[��@}����z�U�۵RS�D˩5{ҙ2�I�e߰�'T+%lB����z���|9�>�4�It�W���h��H<3Z���̣���[#1�!����5\��:wt�cg$/蠹�מ_�p���d�>��'m�y����oޫ�`�q�@�QT�GM4<�"�UAI��:�c9���wK8�Yj��!��|a�J��i��o������D�N�:w�?ʾ�����ZK�}�!��mх~����}�L��2��,$�{�s&:�m�Fa�c�>ҩ�]��o�M��j�>�8�T�Z�/�"����&(ɻ�(zeY1H뙛9��i�˫��.�(�-�ɾ!�U��e�n�_r"�ӷ�7�-W�|�G/k��V#?R�RK���|{j�fL���#r�ym����4�ހ0I/uN�҉[���D�Ŭ2D1rkδɓު�Ƭ�?�� +-���X�ɕ�4��J��6�+<7g+8�w�Z��2}\�ٿg团�������%��9��ự�,.�<rw%���:�t\�_cV,���ۼV+�����������of�I�G�1���)SZh��۸��=�,zS��.�tP u��E�Ͳ�4�0�v��b򍊭�n��y�r���~����6t�M�!�|�1G�l�x�� m�X{>%���u]�^�fk���x��R���?�AmzMr���{q�F�ʗo?��\G�b��t�3�s�	�������f�����H��E�9kV~D�]�Wd��u�_�m�NS����;N�o�˩��|K�XR�l�m���0�]�x��l�.{-�^ȁ��x'��&O��,���h1��/}P��J�g1�3 ���إ��!�z���k����6�n
Q0��Ez}�����dԮ|
�.Jb��HK��>�*G�ZO��jjn���_�,��T/S�h+6"k�jV0<�A���/<�㬕�ZVb�b��b��u�����Yr����e徍du}6��ǢY�j�8+�����s�s����l����a��v�_�}s8��E��!��Q����l��wE��Ҳ�J��w�����h�	��ڄי �ó�%�}oj�M��
(˹6�[;;;�.�J      �   f   x����	�0���d�N x��aj7P���P(;��F�#$�?�IO�� �8��@8�,��M�H�Q�#�fC'¡`U6I�`�yn��̛P��R�ս&Qӵc���UN     