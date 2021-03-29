# Generated by Django 3.0.5 on 2021-03-28 22:59

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='DatosComprador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_Completo', models.CharField(max_length=240)),
                ('codigo_postal', models.CharField(max_length=240)),
                ('localidad_Provincia_Pais', models.CharField(max_length=240)),
                ('email', models.EmailField(max_length=254)),
                ('direccion', models.CharField(max_length=240)),
                ('numero_de_telefono', models.CharField(max_length=240)),
                ('numero_de_movil', models.CharField(max_length=240)),
                ('documento_identidad', models.CharField(max_length=240)),
            ],
        ),
        migrations.CreateModel(
            name='DatosVehiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.CharField(max_length=240)),
                ('marca', models.CharField(max_length=240)),
                ('modelo', models.CharField(max_length=240)),
                ('alimentacion', models.CharField(max_length=240)),
                ('clase_de_cont', models.CharField(max_length=240)),
                ('prime_matr', models.DateField()),
                ('potencia_KW', models.CharField(max_length=240)),
                ('nro_propietarios_Privados', models.CharField(max_length=240)),
                ('nro_propietarios_profesionales', models.CharField(max_length=240)),
                ('cilindrada', models.CharField(max_length=240)),
                ('color', models.CharField(max_length=240)),
                ('fecha_entrega', models.DateField()),
                ('fecha_inicio', models.DateField()),
                ('fecha_activacion', models.DateField()),
            ],
            options={
                'verbose_name': 'Datos del vehiculo',
                'verbose_name_plural': 'Datos de los vehiculos',
            },
        ),
        migrations.CreateModel(
            name='Documentacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rueda_repuesto1', models.BooleanField()),
                ('rueda_repuesto2', models.BooleanField()),
                ('kit_inflado', models.BooleanField()),
                ('triangulo_emergencia', models.BooleanField()),
                ('gato', models.BooleanField()),
                ('chaleco_alta_visibilidad', models.BooleanField()),
                ('kit_bombillas', models.BooleanField()),
                ('kit_bombillas_fusibles', models.BooleanField()),
                ('cod_card', models.BooleanField()),
                ('libre_uso_mantenimiento', models.BooleanField()),
                ('ficha_tecnica', models.BooleanField()),
                ('permiso_circulacion', models.BooleanField()),
                ('itv', models.CharField(max_length=240)),
                ('fecha', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ExamenVisual',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carroceria', models.CharField(max_length=240)),
                ('descripcion_carroceria', models.CharField(max_length=240)),
                ('habitaculo_tapiceria_1', models.CharField(max_length=240)),
                ('descripcion_habitaculo_tapiceria_1', models.CharField(max_length=240)),
                ('habitaculo_tapiceria_2', models.CharField(max_length=240)),
                ('descripcion_habitaculo_tapiceria_2', models.CharField(max_length=240)),
                ('asiento_revestimiento_asiento', models.CharField(max_length=240)),
                ('descripcion_asiento_revestimiento_asiento', models.CharField(max_length=240)),
                ('neumaticos_delanteros', models.CharField(max_length=240)),
                ('descripcion_neumaticos_delanteros', models.CharField(max_length=240)),
                ('neumaticos_traseros', models.CharField(max_length=240)),
                ('descripcion_neumaticos_traseros', models.CharField(max_length=240)),
                ('volante_motor', models.CharField(max_length=240)),
                ('explicacion_detallada_volante_motor', models.TextField()),
                ('motor', models.CharField(max_length=240)),
                ('explicacion_detallada_motor', models.TextField()),
                ('sistema_escape', models.CharField(max_length=240)),
                ('explicacion_detallada_sistema_escape', models.TextField()),
                ('embrague', models.CharField(max_length=240)),
                ('explicacion_detallada_embrague', models.TextField()),
                ('alimentacion_inyeccion', models.CharField(max_length=240)),
                ('explicacion_detallada_alimentacion_inyecion', models.TextField()),
                ('cambio', models.CharField(max_length=240)),
                ('explicacion_detallada_cambio', models.TextField()),
                ('moto_arranque_alternador', models.CharField(max_length=240)),
                ('explicacion_detallada_moto_arranque_alternador', models.TextField()),
                ('diferencial_repartidor', models.CharField(max_length=240)),
                ('explicacion_detallada_diferencial_repartidor', models.TextField()),
                ('caja_transferencia', models.CharField(max_length=240)),
                ('explicacion_detallada_caja_transferencia', models.TextField()),
                ('organo_direccion', models.CharField(max_length=240)),
                ('explicacion_detallada_organo_direccion', models.TextField()),
                ('rodamiento_neumaticos', models.CharField(max_length=240)),
                ('explicacion_detallada_rodamiento_neumaticos', models.TextField()),
                ('direccion_asistida', models.CharField(max_length=240)),
                ('explicacion_detallada_direccion_asistida', models.TextField()),
                ('bomba_direccion_asistida', models.CharField(max_length=240)),
                ('explicacion_detallada_bomba_direccion_asistida', models.TextField()),
                ('sistema_frenado', models.CharField(max_length=240)),
                ('explicacion_detallada_sistema_frenado', models.TextField()),
                ('sistema_refrigeracion', models.CharField(max_length=240)),
                ('explicacion_detallada_sistema_refrigeracion', models.TextField()),
                ('sistema_calefaccion', models.CharField(max_length=240)),
                ('explicacion_detallada_sistema_calefaccion', models.TextField()),
                ('aire_acondicionado', models.CharField(max_length=240)),
                ('explicacion_detallada_aire_acondicionado', models.TextField()),
                ('abs_esp', models.CharField(max_length=240)),
                ('explicacion_detallada_abs_esp', models.TextField()),
                ('cuadro_instrumentos', models.CharField(max_length=240)),
                ('explicacion_detallada_cuadro_instrumentos', models.TextField()),
                ('limpiaparabrisas', models.CharField(max_length=240)),
                ('explicacion_detallada_limpiaparabrisas', models.TextField()),
                ('bomba_limpiaparabrisas', models.CharField(max_length=240)),
                ('explicacion_detallada_bomba_limpiaparabrisas', models.TextField()),
                ('sistema_electrico', models.CharField(max_length=240)),
                ('explicacion_detallada_sistema_electrico', models.TextField()),
                ('cierre_centralizado', models.CharField(max_length=240)),
                ('explicacion_detallada_cierre_centralizado', models.TextField()),
                ('alumbrado_señalizacion', models.CharField(max_length=240)),
                ('explicacion_detallada_alumbrado_señalizacion', models.TextField()),
                ('radio_lectorCD', models.CharField(max_length=240)),
                ('explicacion_detallada_radio_lectorCD', models.TextField()),
                ('navegador', models.CharField(max_length=240)),
                ('explicacion_detallada_navegador', models.TextField()),
                ('elevalunas_electrico', models.CharField(max_length=240)),
                ('explicacion_detallada_elevalunas_electrico', models.TextField()),
                ('airbag', models.CharField(max_length=240)),
                ('explicacion_detallada_airbag', models.TextField()),
                ('antirrobo', models.CharField(max_length=240)),
                ('explicacion_detallada_antirrobo', models.TextField()),
                ('techo_solar', models.CharField(max_length=240)),
                ('explicacion_detallada_techo_solar', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Mantenimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado_revisiones', models.CharField(max_length=240)),
                ('mantenimiento_previo_entrega', models.CharField(max_length=240)),
                ('correa_servicio', models.CharField(max_length=240)),
                ('estado_bateria', models.CharField(max_length=240)),
                ('correa_distribucion', models.CharField(max_length=240)),
                ('ultimo_mantenimiento', models.CharField(max_length=240)),
                ('proximo_mantenimiento', models.CharField(max_length=240)),
                ('ultima_ITV', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Suplemento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuatro_por_cuatro', models.BooleanField()),
                ('super_Car', models.BooleanField()),
                ('cambio_autom', models.BooleanField()),
                ('suv', models.BooleanField()),
                ('vehiculo_comercial', models.BooleanField()),
                ('cobertura', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('concesionario', models.CharField(max_length=240)),
                ('insercion_de_Vehiculo', models.CharField(max_length=240)),
                ('duracion_del_contrato', models.CharField(max_length=240)),
                ('datos_del_Vehiculo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='formApp.DatosVehiculo')),
                ('datos_del_comprador', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='formApp.DatosComprador')),
                ('documentacion', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='formApp.Documentacion')),
                ('examen_visual', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='formApp.ExamenVisual')),
                ('mantenimiento', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='formApp.Mantenimiento')),
                ('suplementos', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='formApp.Suplemento')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone', models.CharField(max_length=12)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'db_table': 'auth_user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
